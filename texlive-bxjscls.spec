# revision 28901
# category Package
# catalog-ctan /language/japanese/BX/bxjscls
# catalog-date 2012-12-21 17:28:17 +0100
# catalog-license other-free
# catalog-version 0.3a
Name:		texlive-bxjscls
Version:	0.3a
Release:	2
Summary:	Document classes based on jsclasses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/BX/bxjscls
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjscls.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides classes, based on jsclasses.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxjscls/bxjsarticle.cls
%{_texmfdistdir}/tex/latex/bxjscls/bxjsptex.def
%{_texmfdistdir}/tex/latex/bxjscls/bxjsreport.cls
%doc %{_texmfdistdir}/doc/latex/bxjscls/LICENSE
%doc %{_texmfdistdir}/doc/latex/bxjscls/README
%doc %{_texmfdistdir}/doc/latex/bxjscls/bxjsclasses.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bxjscls/bxjsclasses.dtx
%doc %{_texmfdistdir}/source/latex/bxjscls/bxjsclasses.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
