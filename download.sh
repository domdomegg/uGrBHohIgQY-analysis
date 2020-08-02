# Check for youtube-dl
command -v foo >/dev/null 2>&1 || { echo >&2 "This script requires youtube-dl but it's not installed. See https://ytdl-org.github.io/youtube-dl/download.html"; exit 1; }

# Download the file
# Format 160 is the smallest file there is - will make video analysis easier
youtube-dl -f 160 -o "video.mp4" https://www.youtube.com/watch?v=uGrBHohIgQY