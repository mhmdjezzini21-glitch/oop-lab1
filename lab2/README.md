# Lab 2 — Automotive Parts Manufacturing Plant

An object-oriented implementation of an automotive parts manufacturing plant in Python.
The system manages employees, production lines, inventory, customer orders, finance, and quality control.

## Metrics

| Metric | Value |
|---|---|
| Classes | 52 |
| Fields | 165 |
| Behaviors | 110 |
| Associations | 42 |
| Exceptions | 16 |

## Classes

| Class | Fields | Methods | Associations (related classes) |
|---|---|---|---|
| Employee | 4 | 3 | Shift |
| Worker | 3 | 1 | Employee |
| Engineer | 3 | 1 | Employee, Part |
| Manager | 3 | 2 | Employee |
| Shift | 3 | 3 | Worker |
| Part | 4 | 2 | — |
| EnginePart | 5 | 1 | Part |
| BrakePart | 5 | 1 | Part |
| SuspensionPart | 5 | 1 | Part |
| ElectricalPart | 5 | 1 | Part |
| Machine | 6 | 4 | ProductionLine |
| ProductionLine | 3 | 5 | Machine |
| ProductionOrder | 5 | 3 | ProductionLine |
| Customer | 3 | 0 | Order |
| OrderLine | 3 | 1 | Part |
| Order | 4 | 5 | Customer, OrderLine |
| StorageBin | 4 | 3 | Warehouse |
| Warehouse | 3 | 5 | StorageBin, Part |
| Account | 2 | 2 | Transaction |
| Transaction | 5 | 1 | Account |
| Supplier | 4 | 1 | SupplierRegistry |
| Invoice | 3 | 1 | — |
| SupplierRegistry | 1 | 3 | Supplier |
| QualityStandard | 2 | 0 | QualityCheck |
| QualityCheck | 5 | 3 | QualityStandard |
| Plant | 10 | 12 | All of the above |
| ProductionService | 0 | 1 | ProductionOrder, ProductionLine |
| InventoryService | 1 | 1 | Warehouse, Order |
| FinanceService | 1 | 2 | Plant, Order, Account |
| Exceptions (16) | 0 | 0 | PlantException |

## Exceptions (16)
- PlantException
- InvalidPartDataException
- PartNotFoundException
- InsufficientStockException
- MachineFailureException
- MachineNotFoundException
- InvalidOrderDataException
- OrderNotFoundException
- InvalidEmployeeDataException
- EmployeeNotFoundException
- InsufficientFundsException
- QualityCheckFailedException
- SupplierNotFoundException
- InvalidShiftException
- CapacityExceededException

## How to run

```bash
pip install -r requirements.txt
python -m src.cli.main
pytest