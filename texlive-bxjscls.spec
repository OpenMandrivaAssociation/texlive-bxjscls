%global tl_name bxjscls
%global tl_revision 79198

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9f
Release:	%{tl_revision}.1
Summary:	Japanese document class collection for all major engines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxjscls
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an extended version of the Japanese document class
collection provided by jsclasses. While the original version supports
only pLaTeX and upLaTeX, the extended version also supports pdfLaTeX,
XeLaTeX and LuaLaTeX, with the aid of suitable packages that provide
capability of Japanese typesetting.

