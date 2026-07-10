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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The biocon--biological conventions--package aids the typesetting of some
biological conventions. At the moment, it makes a good job of
typesetting species names (and ranks below the species level). A
distinction is made between the Plant, Fungi, Animalia and Bacteria
kingdoms. There are default settings for the way species names are
typeset, but they can be customized. Different default styles are used
in different situations.

