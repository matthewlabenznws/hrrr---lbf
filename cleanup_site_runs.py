import os
import shutil


KEEP_COUNTS = {
    ("hrrr", "refl_uh"): 8,
    ("hrrr", "hail_swath"): 8,
    ("rrfs", "refl_uh"): 8,
    ("rrfs", "hail_swath"): 8,
}


def cleanup_runs(model, product, keep):
    base_dir = os.path.join("site", "runs", model, product)

    if not os.path.exists(base_dir):
        print(f"Skipping missing directory: {base_dir}")
        return

    runs = sorted(
        [
            d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))
        ],
        reverse=True
    )

    old_runs = runs[keep:]

    for run in old_runs:
        path = os.path.join(base_dir, run)
        print(f"Removing old run: {path}")
        shutil.rmtree(path, ignore_errors=True)


for (model, product), keep in KEEP_COUNTS.items():
    cleanup_runs(model, product, keep)
