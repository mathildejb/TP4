import os

good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")
print("Le premier commit défectueux est:")
os.system("git show --quiet $(git bisect log | grep 'first bad commit' -A 1 | tail -n 1)")

os.sytem("git bisect reset")