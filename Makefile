# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

PDFVIEWER = explorer.exe

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	
surge:
	surge build/html/ ini-prog.surge.sh

		
spelling:
	@echo Serving pages on $(SPHINX_URL)
	sphinx-build -b spelling -d build/doctrees   source $(BUILDDIR)/spelling

view:
	$(PDFVIEWER) ./build/latex/tm-ecrit.pdf

tmpdf:
	make latex
	# curl https://gist.githubusercontent.com/donnerc/ceb6e0045d108f41e702/raw/sphinxmanual.cls > build/latex/sphinxmanual.cls
	# curl
	# https://gist.githubusercontent.com/donnerc/ceb6e0045d108f41e702/raw/Makefile
	# > build/latex/Makefile
	cp -f latex-templates/Makefile $(BUILDDIR)/latex
	cp -f latex-templates/sphinxmanual.cls $(BUILDDIR)/latex
	cd build/latex/ && make

getpdf:
	cp -f build/latex/tm-ecrit.pdf .
