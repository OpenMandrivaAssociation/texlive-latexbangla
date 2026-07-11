%global tl_name latexbangla
%global tl_revision 55475

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Enhanced LaTeX integration for Bangla
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/latexbangla
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbangla.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbangla.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package simplifies the process of writing Bangla in LaTeX and
addresses most of the associated typesetting issues. Notable features:
Automated transition from Bangla to English and vice versa. Patch for
the unproportionate whitespace issue in popular Bangla fonts. Full
support for all the common commands and environments. Bangla numbering
for page, section, chapter, footnotes etc. (extending polyglossia's
support). New theorem, problems, example, solution and other
environments, all of which are in Bangla.

