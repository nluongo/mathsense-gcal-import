echo "Running"
cd ~/Code/mathsense-gcal-import
export PATH="$HOME/.local/bin:$PATH"
poetry run mathsense-gcal-import > log.txt
