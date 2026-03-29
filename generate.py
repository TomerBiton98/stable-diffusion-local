from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import time
from pathlib import Path

print(" Starting...")

# Config
MODEL_ID   = "runwayml/stable-diffusion-v1-5"
DEVICE     = "mps" if torch.backends.mps.is_available() else "cpu"
DTYPE      = torch.float32          
OUT_DIR    = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

SEED       = 42
STEPS = 30
CFG = 8.0                   
N_IMAGES   = 3
WIDTH = 832
HEIGHT = 512

print(f"Device : {DEVICE}")
print(f"Canvas : {WIDTH}×{HEIGHT}  |  Steps: {STEPS}  |  CFG: {CFG}")

#  Pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=DTYPE,
    safety_checker=None,
    requires_safety_checker=False,
)

pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config,
    algorithm_type="dpmsolver++",
    use_karras_sigmas=True,   
)

pipe.enable_attention_slicing(slice_size="auto")
pipe.enable_vae_slicing()
pipe = pipe.to(DEVICE)

# Warm-up pass 
print("Warming up MPS kernel...")
_ = pipe("test", num_inference_steps=1, width=64, height=64)

print("Model ready")

# Prompts
prompt = (
    "photorealistic dystopian cyberpunk megacity at night seen from inside a ruined luxury penthouse, "
    "cracked floor-to-ceiling rain-covered glass, dark abandoned interior in deep blue-black shadow, "
    "vast skyline of brutalist arcologies, stacked neon skyscrapers, vertical slums, holographic geisha ads, "
    "flying cars and drones between towers, acid rain, toxic fog, steam, volumetric smog, "
    "magenta cyan acid-green neon reflections on wet glass, cinematic lighting, god rays, "
    "sharp distant city detail, anamorphic lens flare, atmospheric perspective, ultra-detailed, masterpiece"
    "view from a silent abandoned penthouse sanctuary overlooking a collapsing cyberpunk empire, "
)


negative_prompt = (
    "worst quality, low quality, low resolution, blurry, soft, noisy, grainy, jpeg artifacts, "
    "flat lighting, washed out, low contrast, overexposed, underexposed, dull colors, "
    "cartoon, anime, cel shading, comic, illustration, painting, watercolor, sketch, stylized, "
    "plastic, fake, cg, unrealistic materials, bad perspective, distorted architecture, warped buildings, "
    "duplicate buildings, malformed vehicles, floating objects, messy composition, empty scene, sparse skyline, "
    "clean utopia, bright daylight, sunny, cheerful, minimalist city, suburban, ordinary skyline, "
    "text, watermark, logo, frame, border, people close-up, portrait, character focus"
)

#  Generate 
print(f"Generating {N_IMAGES} images...")

# One generator per image gives cleaner
generators = [
    torch.Generator(device=DEVICE).manual_seed(SEED + i)
    for i in range(N_IMAGES)
]

start = time.time()

for i, gen in enumerate(generators):
    img_start = time.time()
    result = pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=STEPS,
        guidance_scale=CFG,
        width=WIDTH,
        height=HEIGHT,
        generator=gen,
    ).images[0]

    out_path = OUT_DIR / f"cyberpunk_{SEED + i}.png"
    result.save(out_path)
    print(f"  [{i+1}/{N_IMAGES}] saved → {out_path}  ({round(time.time()-img_start, 1)}s)")

print(f"\n All done in {round(time.time()-start, 1)}s  →  ./{OUT_DIR}/")
