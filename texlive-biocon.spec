%global tl_name biocon
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesetting biological species names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biocon
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The biocon--biological conventions--package aids the typesetting of some
biological conventions. At the moment, it makes a good job of
typesetting species names (and ranks below the species level). A
distinction is made between the Plant, Fungi, Animalia and Bacteria
kingdoms. There are default settings for the way species names are
typeset, but they can be customized. Different default styles are used
in different situations.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biocon
%dir %{_datadir}/texmf-dist/tex/latex/biocon
%doc %{_datadir}/texmf-dist/doc/latex/biocon/COPYING
%doc %{_datadir}/texmf-dist/doc/latex/biocon/INSTALL
%doc %{_datadir}/texmf-dist/doc/latex/biocon/README
%doc %{_datadir}/texmf-dist/doc/latex/biocon/biocon.nw
%doc %{_datadir}/texmf-dist/doc/latex/biocon/literature.bib
%doc %{_datadir}/texmf-dist/doc/latex/biocon/manual-old.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biocon/manual-old.tex
%doc %{_datadir}/texmf-dist/doc/latex/biocon/manual.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biocon/manual.tex
%doc %{_datadir}/texmf-dist/doc/latex/biocon/source.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biocon/source.tex
%{_datadir}/texmf-dist/tex/latex/biocon/biocon-old.sty
%{_datadir}/texmf-dist/tex/latex/biocon/biocon.sty
