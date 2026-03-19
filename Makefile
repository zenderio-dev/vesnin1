.DEFAULT_GOAL := help

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "creating practice"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "removing practice"
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"


# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md
