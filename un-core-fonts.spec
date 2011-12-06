%global fontname un-core
%global fontconf 65-0-%{fontname}

%global alphatag    080608
%global archivename un-fonts-core-%{version}-%{alphatag}

%global common_desc \
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Core set is composed of: \
\
- UnBatang: serif \
- UnDinaru: fantasy \
- UnDotum: sans-serif \
- UnGraphic: sans-serif style \
- UnGungseo: cursive, brush-stroke \
- UnPilgi: script

%define common_desc_ko \
은글꼴 시리즈는 HLaTex개발자이신 은광희님이 1998년에 개발한 폰트입니다. \
2003년에 박원규님이 FontForge를 이용하여 트루타입폰트로 변환했습니다. \
은글꼴은 가장 일반적인 글꼴들입니다. \
\
Core 모음: \
- 은바탕: serif \
- 은디나루: fantasy \
- 은돋음: sans-serif \
- 은그래픽: sans-serif style \
- 은궁서: cursive, brush-stroke \
- 은필기: script

Name:           %{fontname}-fonts
Version:        1.0.2
Release:        0.15.%{alphatag}%{?dist}
Summary:        Un Core family of Korean TrueType fonts
Summary(ko):    한글 은글꼴 Core 모음

Group:          User Interface/X
License:        GPLv2
URL:            http://kldp.net/projects/unfonts/
Source0:        http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source1:        %{name}-batang-fontconfig.conf
Source2:        %{name}-dinaru-fontconfig.conf
Source3:        %{name}-dotum-fontconfig.conf
Source4:        %{name}-graphic-fontconfig.conf
Source5:        %{name}-gungseo-fontconfig.conf
Source6:        %{name}-pilgi-fontconfig.conf
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%package common
Summary:        Common files of Un Core fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

# un_subpkg 1:name 2:Name 3:Hangul [4:obsolete] [5:obsolete]
%define un_subpkg() \
%package -n %{fontname}-%1-fonts \
Summary:        Un Core fonts - %(echo %2) \
Summary(ko):    한글 은글꼴 Core 모음 - %(echo %3) \
Group:          User Interface/X \
Requires:       %{name}-common = %{version}-%{release} \
Obsoletes:      un-core-fonts-%1 < 1.0.2-0.9, %{?4:un-core-fonts-%{1}%{4} < 1.0.2-0.9},  %{?5:un-core-fonts-%{1}%{5} < 1.0.2-0.9} \
\
\

%un_subpkg batang UnBatang 은바탕 bold
%un_subpkg dinaru UnDinaru 은디나루 bold light
%un_subpkg dotum UnDotum 은돋음 bold
%un_subpkg graphic UnGraphic 은그래픽 bold
%un_subpkg gungseo UnGungseo 은궁서
%un_subpkg pilgi UnPilgi 은필기 bold


%description
%common_desc

%description -l ko
%common_desc_ko

%description -n %{fontname}-batang-fonts
%common_desc

This package includes UnBatang, a serif font.

%description -l ko -n %{fontname}-batang-fonts
%common_desc_ko

이 패키지에는 은바탕글꼴이 포함되어 있습니다.

%description -n %{fontname}-dinaru-fonts
%common_desc

This package includes UnDinaru, a fantasy font.

%description -l ko -n %{fontname}-dinaru-fonts
%common_desc_ko

이 패키지에는 은디나루글꼴이 포함되어 있습니다.

%description -n %{fontname}-dotum-fonts
%common_desc

This package includes UnDotum, a sans-serif font.

%description -l ko -n %{fontname}-dotum-fonts
%common_desc_ko

이 패키지에는 은돋음글꼴이 포함되어 있습니다.

%description -n %{fontname}-graphic-fonts
%common_desc

This package includes UnGraphic, a sans-serif font.

%description -l ko -n %{fontname}-graphic-fonts
%common_desc_ko

이 패키지에는 은그래픽글꼴이 포함되어 있습니다.

%description -n %{fontname}-gungseo-fonts
%common_desc

This package includes UnGungseo, a cursive font.

%description -l ko -n %{fontname}-gungseo-fonts
%common_desc_ko

이 패키지에는 은궁서글꼴이 포함되어 있습니다.

%description -n %{fontname}-pilgi-fonts
%common_desc

This package includes UnPilgi, a script font.

%description -l ko -n %{fontname}-pilgi-fonts
%common_desc_ko

이 패키지에는 은필기글꼴이 포함되어 있습니다.


%_font_pkg -n batang -f %{fontconf}-batang.conf UnBatang.ttf UnBatangBold.ttf
%_font_pkg -n dinaru -f %{fontconf}-dinaru.conf UnDinaru.ttf UnDinaruLight.ttf UnDinaruBold.ttf
%_font_pkg -n dotum -f %{fontconf}-dotum.conf UnDotum.ttf UnDotumBold.ttf
%_font_pkg -n graphic -f %{fontconf}-graphic.conf UnGraphic.ttf UnGraphicBold.ttf
%_font_pkg -n gungseo -f %{fontconf}-gungseo.conf UnGungseo.ttf
%_font_pkg -n pilgi -f %{fontconf}-pilgi.conf UnPilgi.ttf UnPilgiBold.ttf


%prep
%setup -q -n un-fonts


%build


%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-batang.conf
install -m 0644 -p %{SOURCE2}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dinaru.conf
install -m 0644 -p %{SOURCE3}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dotum.conf
install -m 0644 -p %{SOURCE4}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-graphic.conf
install -m 0644 -p %{SOURCE5}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gungseo.conf
install -m 0644 -p %{SOURCE6}\
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pilgi.conf

for fconf in %{fontconf}-batang.conf \
    %{fontconf}-dinaru.conf \
    %{fontconf}-dotum.conf \
    %{fontconf}-graphic.conf \
    %{fontconf}-gungseo.conf \
    %{fontconf}-pilgi.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -rf %{buildroot}


%files common
%defattr(0644,root,root,0755)
%doc COPYING README


%changelog
* Tue May 25 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.15.080608
- fix trivial typos in fontconfig config files (thanks Akira TAGOH)

* Wed May 12 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.14.080608
- add "ko" as well as "ko-kr" to the lang test of .conf files to avoid
  some glyphs to be rendered with wqy-zenhei-fonts

* Thu May  6 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.13.080608
- assign higher priority (65- -> 65-0-) to .conf files to avoid the
  effects of 65-nonlatin.conf
- remove binding="same" from .conf files

* Tue May  4 2010 Jens Petersen <petersen@redhat.com> - 1.0.2-0.12.080608
- update .conf files to be locale-specific (#586877)

* Mon Apr 26 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-0.11.080608
- use _font_pkg macro (#581734)
- don't install un-core-fonts-*{light,bold}-fontconfig.conf

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.10.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.9.080608
- update to new fonts packaging and naming (#477474)
- moved bold (and light) weights into main subpackages (#468618)
- add obsoletes for renaming and former bold subpackages (#468618)

* Fri Jun 26 2009 Jens Petersen <petersen@redhat.com> - 1.0.2-0.8.080608
- fix filelist to only include specific font (#496795)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.7.080608
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 14 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.6.080608
- fixed subpackage description and fontconfig.

* Wed Jul 16 2008 Jens Petersen <petersen@redhat.com> - 1.0.2-0.5.080608
- add subpackages with a macro

* Mon Jul 07 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.4.080608
- Refined .spec literal

* Sun Jul 06 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.3.080608
- Added or Changed a Summary and Description.
- Removed nil item.
- Refined versioning contents.
- Renamed from un-fonts-core.spec

* Thu Jul 03 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.2.080608
- Refined .spec literal, license, versioning contents.

* Sat Jun 28 2008 Dennis Jang <smallvil@get9.net> - 1.0.2-0.1.080608
- Initial release.
