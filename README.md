# bot-playbook

Sample projects for acceptance rounds of the department bot: Issue and pull request review, automatic development, workflows, CI gates, releases and Actions failure analysis. Each round resets `main` to the `seed` tag; Issues and pull requests from earlier rounds are closed, not reused.

The repository has no `.bot/` rule files on purpose, so the bot starts from its built-in rules.

## Projects

| Directory | Language | What it is |
| --- | --- | --- |
| `inventory/` | Python 3.11, standard library only | An in-memory stock ledger: receive, ship, value and low-stock queries |
| `textkit/` | Node.js 22, ES modules, no dependencies | Text helpers: URL slugs and title case |

Both projects have known defects that the tests do not cover, so that reviews and development have something real to find.

## Tests

```sh
sh scripts/test.sh
```

The script runs, from any directory, `python3 -m unittest` for `inventory/` and `node --test` for `textkit/`. The `ci` workflow runs the same script on pull requests and on `main`.

## Actions probes

The `actions-probe-*` workflows only run by hand (`workflow_dispatch`) and fail on purpose, one per failure class:

| Workflow | How it fails |
| --- | --- |
| `actions-probe-code` | A failing assertion in the repository's own check |
| `actions-probe-external-flaky` | A network timeout on the first attempt only; a rerun passes |
| `actions-probe-external-down` | A network timeout on every attempt |
| `actions-probe-unknown` | An exit code without a recognizable cause |

## Labels

The repository's labels are the bot's label list: `type/*`, `source/*`, `priority/*`, `area/*` and `size/*`, each with a description, plus `bot-develop`. The bot only adds labels that already exist here, never changes an axis a person has already set, and never adds `priority/critical` or `bot-develop`; those are for people.
