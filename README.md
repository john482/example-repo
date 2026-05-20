# Nike Shoe Inventory Manager

A command-line inventory management system built in Python using Object-Oriented Programming (OOP) principles.

## Description

This program manages a shoe inventory stored in a local text file (`inventory.txt`). It uses a `Shoe` class to represent individual stock items and provides a menu-driven interface to perform the following operations:

- View all shoes in a formatted table
- Capture and add a new shoe to the inventory
- Search for a shoe by its stock code
- Restock the item with the lowest quantity
- Calculate the total value per item (cost × quantity)
- Identify the highest quantity item (flagged for sale)
- Reload data from the inventory file

Data is read from and written back to a `.txt` file in CSV format.

## Files

- [inventory.py](inventory.py) — Main program
- [inventory.txt](inventory.txt) — Inventory data file (CSV format)
