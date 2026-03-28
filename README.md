# 🧠 Local Stable Diffusion Image Generator (Mac MPS Optimized)

A lightweight, script-based pipeline for generating **images locally** using Stable Diffusion.

This project focuses on **understanding and engineering** a local generative AI workflow — not just using it.

---

## 🚀 Overview

This repository implements a fully local text-to-image pipeline using:

* Stable Diffusion v1.5
* Hugging Face Diffusers
* PyTorch (Apple Metal / MPS)

The system takes a natural language prompt and generates high-quality images **directly on your machine**, without relying on cloud APIs or heavy web interfaces.

---

## ✨ Key Features

* 🖥 **Fully local execution** (no external APIs)
* ⚡ **Optimized for Apple Silicon (M1/M2/M3 via MPS)**
* 🎯 **Photorealistic prompt engineering (reduced “AI look”)**
* 🔁 **Batch generation with reproducible seeds**
* 🧠 **Advanced scheduler (DPM++ Karras) for higher detail**
* 💾 **Organized output system**
* 🧩 **Modular, clean Python structure**

---

## 🧱 Tech Stack

| Component    | Technology             |
| ------------ | ---------------------- |
| Language     | Python 3.10            |
| ML Framework | PyTorch                |
| Diffusion    | Hugging Face Diffusers |
| Model        | Stable Diffusion v1.5  |
| Hardware     | Apple Silicon (MPS)    |

---

## 📁 Project Structure

```
stable-diffusion-local/
├── generate.py        # Main generation pipeline
├── requirements.txt   # Dependencies
├── outputs/           # Generated images (ignored by git)
├── README.md
└── .gitignore
```

---

## 🧠 How It Works

The pipeline follows a simple but powerful flow:

```
Prompt → Diffusion Model → Image → Saved Locally
```

### Key optimizations:

* **DPMSolver++ scheduler (Karras)**
  Improves detail and realism at lower step counts

* **Attention slicing + VAE slicing**
  Reduces memory usage (important for MPS)

* **Warm-up pass**
  Eliminates first-run latency due to Metal compilation

* **Seed control**
  Enables reproducible outputs and controlled variation

---

## 🎯 Prompt Engineering Strategy

This project focuses heavily on Prompt Engineering to improve output.
Instead of simple prompts, it uses layered prompting:

### Structure:

* Scene (environment + composition)
* Lighting (cinematic, volumetric)
* Camera simulation (lens, exposure)
* Imperfections (film grain, noise)
* Style references (cinematography, mood)

### Example prompt:

```text
photorealistic dystopian cyberpunk megacity at night seen from inside a ruined penthouse,
cracked rain-covered glass, dark interior, dense neon skyline, flying vehicles, fog,
cinematic lighting, realistic exposure, depth of field, subtle film grain
```

---

## ⚡ Performance

Typical performance on Mac M1/M2:

| Setting    | Result                   |
| ---------- | ------------------------ |
| Resolution | 832×512                  |
| Steps      | 25–30                    |
| Time       | ~25–60 seconds per image |

---

## 🚀 Future Improvements

* 🔥 Upgrade to **SDXL** (higher realism)
* 🧠 LLM-based prompt enhancement
* 🎛 ControlNet integration (scene control)
* 🌐 Web interface (React / FastAPI)
* 📦 CLI tool for dynamic prompting

---

## 📸 Example Output
---



## first rub 
First Run
<img width="512" height="512" alt="output_0" src="https://github.com/user-attachments/assets/2f19be72-154f-4712-bc23-5683ed639464" />

Second Run
<img width="768" height="512" alt="cyberpunk_44" src="https://github.com/user-attachments/assets/20dee3dd-2739-4027-8891-7e7dc48375b2" />

Third Run
<img width="768" height="512" alt="cyberpunk_42 2" src="https://github.com/user-attachments/assets/4c9b79f2-f167-4760-afaa-b78faf1dae9d" />

Fourth Run
<img width="832" height="512" alt="cyberpunk_43 3" src="https://github.com/user-attachments/assets/ae5dfe07-88ab-4fa4-a083-271ee83903c7" />

---

## 🧑‍💻 Why This Project

This project was built to:

* Understand how diffusion models actually work locally
* Build a clean, controllable AI pipeline
* Move from “AI user” → **AI system builder**

---

## 📜 License

This project uses Stable Diffusion under its respective license.
Ensure compliance when using outputs publicly.

---

## 🙌 Author

Built as part of a hands-on exploration of **local generative AI systems**, focusing on performance, realism, and system design.
