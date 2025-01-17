import json, argparse, pathlib

DB = pathlib.Path("todos.json")

def load():
    return json.loads(DB.read_text()) if DB.exists() else []

def save(items):
    DB.write_text(json.dumps(items, indent=2))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")

    addp = sub.add_parser("add"); addp.add_argument("text")
    sub.add_parser("list")
    donep = sub.add_parser("done"); donep.add_argument("index", type=int)

    args = p.parse_args()
    items = load()

    if args.cmd == "add":
        items.append({"text": args.text, "done": False})
        save(items); print("Added.")
    elif args.cmd == "list":
        for i, it in enumerate(items):
            status = "✓" if it["done"] else " "
            print(f"{i}: [{status}] {it['text']}")
    elif args.cmd == "done":
        items[args.index]["done"] = True; save(items); print("Done.")

if __name__ == "__main__":
    main()
