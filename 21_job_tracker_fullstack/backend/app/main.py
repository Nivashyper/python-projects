from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from .database import init_db, get_session
from .models import User, Job
from .schemas import UserCreate, Token, JobCreate, JobRead
from .auth import hash_password, verify_password, create_access_token, get_current_user

app = FastAPI(title="Job Tracker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/auth/register", response_model=Token)
def register(data: UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == data.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=data.email, password_hash=hash_password(data.password))
    session.add(user); session.commit()
    token = create_access_token(sub=user.email)
    return Token(access_token=token)

@app.post("/api/auth/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form.username)).first()
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(sub=user.email)
    return Token(access_token=token)

@app.post("/api/jobs", response_model=JobRead)
def create_job(job: JobCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    obj = Job(**job.dict(), owner_id=user.id)
    session.add(obj); session.commit(); session.refresh(obj)
    return JobRead(id=obj.id, **job.dict())

@app.get("/api/jobs", response_model=list[JobRead])
def list_jobs(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    items = session.exec(select(Job).where(Job.owner_id == user.id).order_by(Job.created_at.desc())).all()
    return [JobRead(id=i.id, title=i.title, company=i.company, status=i.status, applied_date=i.applied_date, link=i.link, notes=i.notes) for i in items]

@app.put("/api/jobs/{job_id}", response_model=JobRead)
def update_job(job_id: int, job: JobCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    obj = session.get(Job, job_id)
    if not obj or obj.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Job not found")
    for k, v in job.dict().items():
        setattr(obj, k, v)
    session.add(obj); session.commit(); session.refresh(obj)
    return JobRead(id=obj.id, title=obj.title, company=obj.company, status=obj.status, applied_date=obj.applied_date, link=obj.link, notes=obj.notes)

@app.delete("/api/jobs/{job_id}")
def delete_job(job_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    obj = session.get(Job, job_id)
    if not obj or obj.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Job not found")
    session.delete(obj); session.commit()
    return {"deleted": True, "id": job_id}
