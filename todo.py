todos = [
    {"title": "レポートを提出する", "completed": False, "priority": "高"},
    {"title": "教科書を返却する", "completed": True, "priority": "中"},
]


def show_todos():
    print("TODO一覧")
    print("優先度")

    print("未完了のTODO")
    for todo in todos:
        if not todo["completed"]:
            print(f'- {todo["title"]} [{todo["priority"]}]')

    print("完了したTODO")
    for todo in todos:
        if todo["completed"]:
            print(f'- {todo["title"]} [{todo["priority"]}]')


show_todos()