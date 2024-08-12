# MindAnchor

![MindAnchor Logo](https://github.com/AI2B-uk/MindAnchor/blob/main/MindAnchor.svg)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

## 🫂Contributors

[![Dangerousfish](https://avatars.githubusercontent.com/u/30146283?v=4&s=100)(https://github.com/dangerousfish)]
**Dangerousfish**

MindAnchor is a mental health companion app designed to help users manage their mental well-being through various techniques such as grounding exercises, cognitive restructuring, journaling, and crisis planning. Whether you're dealing with anxiety, stress, or just need a mental health check-in, MindAnchor provides tools and resources to help you stay grounded and focused.

## 🌟 Features

- **Reality Testing**: Challenge and reshape your thoughts to promote a healthier mindset.
- **Grounding Techniques**: Simple exercises to help you stay connected to the present moment.
- **Cognitive Restructuring**: Reframe negative thoughts to reduce their impact.
- **Safe Space**: Create a virtual safe space for relaxation and mental clarity.
- **Crisis Planning**: Prepare in advance for potential mental health crises.
- **Journaling**: Record your thoughts, feelings, and experiences in a secure, personal space.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7+** installed on your machine.
- **Flask** and **Flask-Login** for running the app.
- **SQLite** or another supported database system.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/MindAnchor.git
   cd MindAnchor
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts ctivate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the Application**

   ```bash
   flask run
   ```

6. **Access the Application**

   Open your browser and go to [http://localhost:5000](http://localhost:5000).

## 🛠️ Usage

Once you have the application up and running, you can access the various features directly from the homepage:

- **Reality Testing**: Navigate to the "Reality Testing" section to challenge your thoughts.
- **Grounding**: Use grounding techniques to stay focused.
- **Cognitive Restructuring**: Access tools for reframing negative thoughts.
- **Safe Space**: Set up and customise your own virtual safe space.
- **Crisis Planning**: Prepare and store your crisis plan securely.
- **Journal**: Write and reflect in your personal journal.

### Dark Mode

MindAnchor supports a dark theme for those who prefer a low-light environment. To switch to dark mode, go to the "Settings" page and toggle the theme switch.

## 📸 Screenshots

### Dashboard

![Dashboard Screenshot](https://path-to-dashboard-screenshot.png)

### Grounding Techniques

![Grounding Screenshot](https://path-to-grounding-screenshot.png)

## 🧩 Contributing

We welcome contributions from the community! To get started:

1. **Fork the Repository**

2. **Create a Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Please make sure to follow the [contribution guidelines](CONTRIBUTING.md) and respect the [code of conduct](CODE_OF_CONDUCT.md).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Acknowledgments

- **Flask** - For providing the core framework for building the app.
- **Flask-Login** - For enabling secure user authentication.
- **SQLite** - For managing our database with ease.
- **Bootstrap** - For making the UI look great.

## 📧 Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/username/MindAnchor/issues) or reach out to the project maintainers at contact@mindanchor.com.

Let's build a healthier mental space together with **MindAnchor**.
