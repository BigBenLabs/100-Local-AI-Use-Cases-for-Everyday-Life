# 100 Local AI Use Cases for Everyday Life

<div align="center">

一个探索实用、隐私友好型本地 AI 应用的开源项目，重点关注个人生产力、学习、创意和自动化等实际场景。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()

**🎯 每一个 AI 应用场景，都值得本地运行**
**🎯 Every AI use case is worth running locally**

[English](#english) | [中文说明](#chinese)

</div>

## 📖 简介

100 Local AI Use Cases for Everyday Life 是一个开源项目，探索在本地运行的实用、隐私友好的 AI 应用场景。每个用例都是模块化、可重现的，专注于实际价值——从个人生产力到学习、创意和自动化。构建、实验，并掌控你的 AI 栈。

**100 Local AI Use Cases for Everyday Life** is an open-source project exploring practical, privacy-friendly AI applications running locally. Each use case is modular, reproducible, and focused on real-world value — from personal productivity to learning, creativity, and automation. Build, experiment, and own your AI stack.

## ✨ 核心特性

- 🏠 **本地运行**: 数据在本地处理，确保隐私和安全
- 🔧 **模块化设计**: 每个 AI 用例独立、可扩展
- 🎯 **实用主义**: 聚焦实际生活和工作中的真实需求
- 🌍 **多语言支持**: 中文、英文等多种语言支持
- 🚀 **快速部署**: 简化的安装和运行流程

### 🏠 Local Execution
Run all AI applications locally on your machine. Your data stays on your device — no cloud APIs, no privacy concerns.

### 🔧 Modular Design
Each use case is self-contained, easy to understand, and ready to customize.

### 🎯 Practical Focus
Focus on real-world applications that solve actual problems in daily life and work.

### 🌍 Multi-language Support
Currently supports Chinese and English, with more languages planned.

### 🚀 Easy Deployment
Simple installation and execution process for each use case.

## 📁 项目结构

```
100-Local-AI-Use-Cases-for-Everyday-Life/
├── apps/                    # 应用示例
│   ├── learning/           # 学习类 AI 应用
│   └── life/               # 生活类 AI 应用
│       └── 00_geo_poetry/  # 地理诗歌生成器
├── core/                    # 核心模块
│   ├── llm.py              # LLM 基础接口
│   └── environment.py      # 环境配置
├── tools/                   # 工具函数
│   └── external_apis.py    # 外部 API 调用
├── LICENSE                  # MIT 许可证
└── README.md                # 项目说明
```

## 🎯 现有用例

### 地理诗歌生成器 (Geo Poetry Generator)

根据地理位置坐标生成诗歌的 AI 应用。

Generate poems based on geographic coordinates using AI.

**已实现功能:**
- 📍 基于经纬度生成地理描述
- 🎭 结合地理信息创作诗歌
- 🌐 支持中英文双语输出

**Implemented Features:**
- 📍 Generate geographic descriptions based on latitude and longitude
- 🎭 Create poems combining geographic information
- 🌐 Support Chinese and English bilingual output

> 更多应用正在开发中...

> More applications are under development...

## 🚀 快速开始

### 前置要求

- Python 3.9 或更高版本
- 可选：Ollama / LocalAI / LM Studio（用于本地 LLM 部署）

### 安装

```bash
# 克隆仓库
git clone https://github.com/BigBenLabs/100-Local-AI-Use-Cases-for-Everyday-Life.git
cd 100-Local-AI-Use-Cases-for-Everyday-Life

# 安装依赖（如果需要）
pip install -r requirements.txt
```

### 运行示例

```bash
# 运行地理诗歌生成器
python apps/life/00_geo_poetry/geo_poetry.py
```

### Quick Start

### Prerequisites

- Python 3.9 or higher
- Optional: Ollama / LocalAI / LM Studio for local LLM deployment

### Installation

```bash
# Clone the repository
git clone https://github.com/BigBenLabs/100-Local-AI-Use-Cases-for-Everyday-Life.git
cd 100-Local-AI-Use-Cases-for-Everyday-Life

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Running an Example

```bash
# Run the Geo Poetry Generator
python apps/life/00_geo_poetry/geo_poetry.py
```

## 🤝 贡献

我们欢迎各种形式的贡献！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

We welcome all forms of contribution!

1. Fork this project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 许可证

本项目采用 [MIT 许可证](LICENSE)。详见 [LICENSE 文件](LICENSE)。

This project is licensed under the [MIT License](LICENSE). See [LICENSE](LICENSE) for details.

## 🙏 致谢

感谢所有为本项目做出贡献的开发者！

Special thanks to all developers who contributed to this project!

## 📧 联系方式

如有问题或建议，欢迎通过 GitHub Issues 联系我们。

If you have any questions or suggestions, feel free to contact us through GitHub Issues.

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个星标！⭐**

Made with ❤️ by BigBenLabs

</div>

---

## English <a id="english"></a>

<div align="center">

**⭐ If this project helps you, please give us a star! ⭐**

Made with ❤️ by BigBenLabs

</div>

### 📖 Introduction

**100 Local AI Use Cases for Everyday Life** is an open-source project exploring practical, privacy-friendly AI applications running locally. Each use case is modular, reproducible, and focused on real-world value — from personal productivity to learning, creativity, and automation. Build, experiment, and own your AI stack.

### ✨ Features

- 🏠 **Local Execution**: Run all AI applications locally on your machine. Your data stays on your device — no cloud APIs, no privacy concerns.
- 🔧 **Modular Design**: Each use case is self-contained, easy to understand, and ready to customize.
- 🎯 **Practical Focus**: Focus on real-world applications that solve actual problems in daily life and work.
- 🌍 **Multi-language Support**: Currently supports Chinese and English, with more languages planned.
- 🚀 **Easy Deployment**: Simple installation and execution process for each use case.

### 📁 Project Structure

```
100-Local-AI-Use-Cases-for-Everyday-Life/
├── apps/                    # Application examples
│   ├── learning/           # Learning AI applications
│   └── life/               # Life AI applications
│       └── 00_geo_poetry/  # Geo Poetry Generator
├── core/                    # Core modules
│   ├── llm.py              # LLM base interface
│   └── environment.py      # Environment configuration
├── tools/                   # Utility functions
│   └── external_apis.py    # External API calls
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

### 🎯 Current Use Cases

### Geo Poetry Generator

An AI application that generates poems based on geographic coordinates.

Generate poems based on geographic coordinates using AI.

**Implemented Features:**
- 📍 Generate geographic descriptions based on latitude and longitude
- 🎭 Create poems combining geographic information
- 🌐 Support Chinese and English bilingual output

### 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Optional: Ollama / LocalAI / LM Studio for local LLM deployment

### Installation

```bash
# Clone the repository
git clone https://github.com/BigBenLabs/100-Local-AI-Use-Cases-for-Everyday-Life.git
cd 100-Local-AI-Use-Cases-for-Everyday-Life

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Running an Example

```bash
# Run the Geo Poetry Generator
python apps/life/00_geo_poetry/geo_poetry.py
```

### 🤝 Contributing

We welcome all forms of contribution!

1. Fork this project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📝 License

This project is licensed under the [MIT License](LICENSE). See [LICENSE](LICENSE) for details.

### 🙏 Acknowledgments

Special thanks to all developers who contributed to this project!

### 📧 Contact

If you have any questions or suggestions, feel free to contact us through GitHub Issues.