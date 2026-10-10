import re
import shutil
from pathlib import Path


WAV_DIR = Path("wav")
LOG_DIR = Path("txt")


def clear_wav_dir(wav_dir: Path = WAV_DIR) -> None:
    if wav_dir.exists():
        shutil.rmtree(wav_dir)
    wav_dir.mkdir(parents=True, exist_ok=True)


def next_log_path(log_dir: Path = LOG_DIR) -> Path:
    log_dir.mkdir(parents=True, exist_ok=True)

    max_n = 0
    for p in log_dir.iterdir():
        if not p.is_file():
            continue
        m = re.compile(r"^log(\d+)\.txt$").match(p.name)
        if m:
            max_n = max(max_n, int(m.group(1)))

    new_path = log_dir / f"log{max_n + 1}.txt"
    new_path.touch(exist_ok=True)
    return new_path


def prepare_run(wav_dir: Path = WAV_DIR, log_dir: Path = LOG_DIR) -> Path:
    clear_wav_dir(wav_dir)
    return next_log_path(log_dir)