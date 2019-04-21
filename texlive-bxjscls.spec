Name:		texlive-bxjscls
Version:	1.9f
Release:	1
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
%{_texmfdistdir}/tex/latex/bxjscls
%doc %{_texmfdistdir}/doc/latex/bxjscls
#- source
%doc %{_texmfdistdir}/source/latex/bxjscls

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
