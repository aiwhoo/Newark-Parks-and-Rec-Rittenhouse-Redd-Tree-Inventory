# Development Workflow

This document outlines the team's development workflow for the Rittenhouse and Redd Tree Inventory project.

## Workflow Steps

```
Repository
    ↓
Clone Project
    ↓
Make Changes
    ↓
Commit Changes
    ↓
Push Changes
    ↓
Open Pull Request
    ↓
Review
    ↓
Merge
```

## Step-by-Step Guide

### Repository
The central location where the project is stored. This is the source of truth for the Rittenhouse and Redd Tree Inventory data and project files on GitHub.

### Clone
Creates a local copy of the project on your machine so you can work on it.

```bash
git clone https://github.com/aiwhoo/Newark-Parks-and-Rec-Rittenhouse-Redd-Tree-Inventory.git
cd Newark-Parks-and-Rec-Rittenhouse-Redd-Tree-Inventory
```

### Make Changes
Edit files, add new data, or update the tree inventory records as needed.

### Commit Changes
A saved checkpoint describing a specific change. Always write clear, descriptive commit messages.

**Example:**
```bash
git commit -m "Update data source for Rittenhouse inventory"
```

**Good commit message practices:**
- Be specific about what changed
- Include the type of change (e.g., Update, Add, Fix)
- Reference the data or feature being modified

### Push Changes
Uploads your local changes to GitHub.

```bash
git push origin main
```

### Open Pull Request
Creates a pull request to allow your changes to be reviewed before being merged into the main project. This ensures code quality and team awareness of changes.

### Review
Team members review the changes, provide feedback, and approve or request modifications.

### Merge
Once approved, the pull request is merged into the main branch, making the changes permanent in the project.

---

**For the Rittenhouse and Redd Tree Inventory project:** Changes typically involve updating tree survey data, adding new tree records, or improving data quality in the `form-1__tree-inventory.csv` file.
