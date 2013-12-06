# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/biocon
# catalog-date 2007-01-23 22:34:44 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-biocon
Version:	20070123
Release:	4
Summary:	Typesetting biological species names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biocon
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biocon.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The biocon--biological conventions--package aids the
typesetting of some biological conventions. At the moment, it
makes a good job of typesetting species names (and ranks below
the species level). A distinction is made between the Plant,
Fungi, Animalia and Bacteria kingdoms. There are default
settings for the way species names are typeset, but they can be
customized. Different default styles are used in different
situations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070123-2
+ Revision: 749745
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070123-1
+ Revision: 717949
- texlive-biocon
- texlive-biocon
- texlive-biocon
- texlive-biocon
- texlive-biocon

