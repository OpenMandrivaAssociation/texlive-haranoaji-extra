Name:		texlive-haranoaji-extra
Version:	68500
Release:	1
Summary:	Harano Aji Fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/haranoaji-extra
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji-extra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji-extra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are
fonts obtained by replacing Adobe-Identity-0 (AI0) CIDs of
Source Han fonts (Source Han Serif and Source Han Sans) with
Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7 weights each for
Mincho and Gothic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/haranoaji-extra
%doc %{_texmfdistdir}/doc/fonts/haranoaji-extra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
