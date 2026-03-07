# Repository Layer — Data Access Rules

## User-scoped data

All user data in the system is **multi-tenant by user**. Every query must be scoped to the authenticated user to prevent cross-user data leakage.

### Rule: Repositories filter by `user_id`

**Every repository method must:**

1. Receive `user_id: str` as a parameter (from `AuthContext.user_id`).
2. Filter all queries by `user_id`:
   - **get** — fetch by id only if it belongs to the user.
   - **list** — filter by `user_id`.
   - **create** — set `user_id` on the entity.
   - **update** — update only if the entity belongs to the user.
   - **delete** — delete only if the entity belongs to the user.

### Example

```python
# Correct: repository receives user_id and filters
async def get_budget_period(repo: BudgetPeriodRepository, period_id: int, user_id: str) -> BudgetPeriod | None:
    return await repo.get_by_id(period_id, user_id=user_id)

# Incorrect: no user scoping
async def get_budget_period(repo: BudgetPeriodRepository, period_id: int) -> BudgetPeriod | None:
    return await repo.get_by_id(period_id)  # WRONG: could leak data across users
```

### Data models

ORM models already include `user_id` on:

- `BudgetPeriodModel`
- `CategoryModel`
- `AllocationModel`
- `TransactionModel`
- `TransferModel`
- `UserSettingsModel`
- `IdempotencyKeyModel`

Repositories must use these columns in every query.
