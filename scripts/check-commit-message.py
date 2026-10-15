#!/usr/bin/env python3
"""Claude Code PreToolUse フック: git commit 実行前に Conventional Commits 規約のリマインダーを注入する。

Bash ツールで `git commit` を実行しようとしたときだけ介入し、
コミットメッセージ規約をモデルの追加コンテキストとして渡す。ブロックはしない。

stdin (JSON):  { "tool_name": "...", "tool_input": { "command": "..." }, ... }
stdout (JSON): { "hookSpecificOutput": { "hookEventName": "PreToolUse", "additionalContext": "..." } }
"""

import json
import re
import sys


REMINDER = (
    "【コミット規約リマインダー】\n"
    "Conventional Commits 形式に従うこと:\n\n"
    "  <type>(<scope>): <subject>\n\n"
    "type   : feat | fix | docs | style | refactor | test | chore | ci | perf | revert\n"
    "scope  : 変更した領域（任意。値はプロジェクトの規約に従う）\n"
    "subject: 命令形・日本語・72 文字以内・末尾ピリオドなし\n\n"
    "例: feat(api): 記事作成エンドポイントを追加する\n"
    "    fix(ui): ログイン後のリダイレクトを修正する\n\n"
    "関連 Issue は footer に Closes #<n> / Refs #<n> を記載する。"
)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    if data.get("tool_name") != "Bash":
        sys.exit(0)

    tool_input = data.get("tool_input", {})
    command = tool_input.get("command", "") if isinstance(tool_input, dict) else ""

    if not re.search(r"\bgit\s+commit\b", command):
        sys.exit(0)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": REMINDER,
        }
    }
    print(json.dumps(output, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
