todos = [
    {"title": "レポートを提出する", "completed": False, "priority": "高"},
    {"title": "教科書を返却する", "completed": True, "priority": "中"},
]


def add_todo(title, priority="中"):
    todos.append({"title": title, "completed": False, "priority": priority})


def show_todos():
    print("TODO一覧")
    print("状態と優先度：高・中・低 / [完了]は完了済み")

    print(f"すべてのTODO（{len(todos)}件）")
    for todo in todos:
        status = "[完了] " if todo["completed"] else ""
        print(f'{status}{todo["title"]} [{todo["priority"]}]')


add_todo("発表資料を作る", "高")
show_todos()