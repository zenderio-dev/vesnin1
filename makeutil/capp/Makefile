.PHONY: another-app
# not all targets are listed in PHONY

# Might correct, but 'build' and 'app' are different targets, so 'build' is not a prerequisite of 'app', and 'app' is not a prerequisite of 'build'. So they are independent targets. If we want to make 'app' depend on 'build', we should write:
build:
	gcc main.c -o app
# correct no PHONY
app: main.c
	gcc main.c -o app

# incorrect: listed in PHONY
another-app: main.c
	gcc main.c -o another-app