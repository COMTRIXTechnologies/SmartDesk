# COMTRIX SmartDesk

**A smarter way to manage your business.**

COMTRIX SmartDesk is a desktop-based business management application developed by **COMTRIX Technologies** to simplify and organize everyday business operations.

Designed with small businesses and retail shops in mind, SmartDesk brings essential business activities together in one convenient application.

---

## About the Project

Managing customers, products, sales, inventory, and daily operations can become complicated as a business grows.

COMTRIX SmartDesk aims to make these activities easier through a centralized, user-friendly desktop application.

The application is being developed with a focus on simplicity, usability, and reliable business data management.

## Features

- **Dashboard** – View business performance, sales summaries, recent transactions, and important alerts.
- **Customer Management** – Maintain customer information.
- **Products & Services** – Manage business products and services.
- **Sales & Orders** – Record and manage sales transactions and orders.
- **Inventory Management** – Monitor stock levels and low-stock items.
- **Task Management** – Organize business tasks.
- **Employee Management** – Maintain employee information.
- **Reports** – Access business reports and sales information.
- **Business Settings** – Configure business profile and application preferences.
- **User Authentication** – Account registration and login.
- **Business Setup** – Configure business information during onboarding.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PySide6 | Desktop graphical user interface |
| SQLite | Local database |
| SQLAlchemy | Database operations and ORM |
| PyInstaller | Windows executable packaging |

## Getting Started

### Requirements

- Windows 10 or Windows 11
- Python 3.13
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/COMTRIXTechnologies/SmartDesk.git
```

**2. Navigate to the project directory**

```bash
cd SmartDesk
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python run.py
```

> Make sure the complete project source folders are present before running the application.

## Project Structure

```text
COMTRIX-SmartDesk/
│
├── app/
│   ├── authentication/
│   ├── onboarding/
│   ├── customers/
│   ├── products/
│   ├── sales/
│   ├── inventory/
│   ├── tasks/
│   ├── employees/
│   ├── reports/
│   └── settings/
│
├── database/
│   ├── database.py
│   └── models.py
│
├── config.py
├── run.py
├── requirements.txt
├── icon.ico
├── pos.jpg
└── README.md
```

*The structure above illustrates the intended organization of the project.*

## Project Status

**Currently in Development**

COMTRIX SmartDesk is actively being developed. Features, improvements, and updates will be added as development progresses.

## Developer

**COMTRIX Technologies**

Building practical technology solutions for businesses.

- **Website:** https://comtrixtechnologies.github.io/website/
- **GitHub:** https://github.com/COMTRIXTechnologies
- **LinkedIn:** https://www.linkedin.com/in/comtrix-technologies-40b705451/

## License

License information will be added when the project license is finalized.

---

© 2026 COMTRIX Technologies. All rights reserved.
