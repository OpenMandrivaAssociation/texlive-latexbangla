Name:		texlive-latexbangla
Version:	55475
Release:	2
Summary:	Enhanced LaTeX integration for Bangla
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexbangla
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbangla.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbangla.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package simplifies the process of writing Bangla in LaTeX
and addresses most of the associated typesetting issues.
Notable features: Automated transition from Bangla to English
and vice versa. Patch for the unproportionate whitespace issue
in popular Bangla fonts. Full support for all the common
commands and environments. Bangla numbering for page, section,
chapter, footnotes etc. (extending polyglossia's support). New
theorem, problems, example, solution and other environments,
all of which are in Bangla.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/latexbangla
%doc %{_texmfdistdir}/doc/latex/latexbangla

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
