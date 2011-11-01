Name:		texlive-biocon
Version:	20070123
Release:	1
Summary:	Typesetting biological species names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biocon
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The biocon--biological conventions--package aids the
typesetting of some biological conventions. At the moment, it
makes a good job of typesetting species names (and ranks below
the species level). A distinction is made between the Plant,
Fungi, Animalia and Bacteria kingdoms. There are default
settings for the way species names are typeset, but they can be
customized. Different default styles are used in different
situations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biocon/biocon-old.sty
%{_texmfdistdir}/tex/latex/biocon/biocon.sty
%doc %{_texmfdistdir}/doc/latex/biocon/COPYING
%doc %{_texmfdistdir}/doc/latex/biocon/INSTALL
%doc %{_texmfdistdir}/doc/latex/biocon/README
%doc %{_texmfdistdir}/doc/latex/biocon/biocon.nw
%doc %{_texmfdistdir}/doc/latex/biocon/literature.bib
%doc %{_texmfdistdir}/doc/latex/biocon/manual-old.pdf
%doc %{_texmfdistdir}/doc/latex/biocon/manual-old.tex
%doc %{_texmfdistdir}/doc/latex/biocon/manual.pdf
%doc %{_texmfdistdir}/doc/latex/biocon/manual.tex
%doc %{_texmfdistdir}/doc/latex/biocon/source.pdf
%doc %{_texmfdistdir}/doc/latex/biocon/source.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
