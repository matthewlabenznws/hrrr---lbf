import os
import shutil


KEEP_COUNTS = {
    ("hrrr", "refl_uh"): 8,
    ("hrrr", "hail_swath"): 8,
    ("rrfs", "refl_uh"): 8,
    ("rrfs", "hail_swath"): 8,
}


def cleanup_runs(model, product, keep):

    base_dir = os.path.abspath(
        os.path.join("site", "runs", model, product)
    )

    print(f"\nCleaning: {base_dir}")

    if not os.path.exists(base_dir):
        print("Directory does not exist.")
        return

    runs = sorted(
        [
            d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))
        ],
        reverse=True
    )

    print(f"Found {len(runs)} runs")

    old_runs = runs[keep:]

    for run in old_runs:
        path = os.path.join(base_dir, run)

        print(f"Removing old run: {path}")

        shutil.rmtree(path, ignore_errors=True)


for (model, product), keep in KEEP_COUNTS.items():
    cleanup_runs(model, product, keep)
