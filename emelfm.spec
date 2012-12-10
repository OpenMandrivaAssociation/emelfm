%define rel 4
%define name emelfm
%define extra_ver 1
%define rversion 0.9.2
%define version 0.9.2.%{extra_ver}
%define extra_ver 1
%define release %mkrel %{rel}

Summary: File manager using the two-panel design and Gtk+
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: File tools
Source: %{name}-%{rversion}-elm%{extra_ver}.tar.bz2 
Url: http://www.havens.de/elm/emelfm.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gtk+-devel >= 1.2
Requires: gtk+ >= 1.2
Requires: xterm

%description
emelFM is a file manager that implements the popular two-panel design. It
features a simple GTK+ interface, a flexible filetyping scheme, and a built-in
command line for executing commands without opening an xterm.

Features:
     o Simple Interface 
     o Bookmarks and History Lists 
     o Flexible filetyping scheme 
     o Multiple actions selectable for each filetype 
     o Filename, Size, and Date Filters 
     o Built-In Command Line 
     o User-defined menu 
     o Configurable Keyboard bindings 
     o Configurable Toolbar 
     o Runtime loadable plugins 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{rversion}-elm%{extra_ver}
##patch0 -p1

%build

%make

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_docdir
mkdir -p $RPM_BUILD_ROOT%_libdir/emelfm/plugins
mkdir -p $RPM_BUILD_ROOT%_datadir/locale/
make BIN_DIR=$RPM_BUILD_ROOT%{_bindir} DOC_DIR=$RPM_BUILD_ROOT%_docdir \
	PLUGINS_DIR=$RPM_BUILD_ROOT%_libdir/emelfm/plugins \
	LOCALEDIR=$RPM_BUILD_ROOT%_datadir/locale/ install

rm -rf $RPM_BUILD_ROOT%_docdir/help.txt
 

mkdir -p   %buildroot%{_datadir}/applications/
 cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Name=Emelfm
Comment=A GTK file manager
Icon=file_tools_section
Categories=X-MandrivaLinux-System-FileTools;System;
EOF

%find_lang %name

%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%{update_menus}      
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr (-,root,root)
%doc README COPYING ChangeLog
%doc docs/help.txt
%{_bindir}/*
%{_datadir}/applications/*
%_libdir/emelfm/plugins/*.so
 


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2.1-4mdv2011.0
+ Revision: 618224
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2.1-3mdv2010.0
+ Revision: 428592
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2.1-2mdv2009.0
+ Revision: 222105
- fix XDG menu directory creation & file list
- auto convert menu to XDG
- kill re-definition of %%buildroot on Pixel's request
- import emelfm

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Jun 06 2006 Charles A Edwards <eslrahc@mandriva.org> 0.9.2.1-2mdv2007.0
- mkrel
- rebuild

* Mon Mar 14 2005 Charles A Edwards <eslrahc@mandrake.org> 0.9.2.1-1mdk
- 0.9.2-elm1
- drop patch
- update URL

* Mon Aug 23 2004 Charles A Edwards <eslrahc@mandrake.org> 0.9.2-7mdk
- rebuild for new menu

* Thu Apr 01 2004 Charles A Edwards <eslrahc@mandrake.org> 0.9.2-6mdk
- Require xterm
- fix menu entry

* Thu Oct 16 2003 <Charles A Edwards <eslrahc@bellsouth.net> 0.9.2-5mdk
- update Patch for correct doc location
- adjust echo script

* Mon Jun 23 2003 Götz Waschk <waschk@linux-mandrake.com> 0.9.2-4mdk
- from Charles A Edwards <eslrahc@bellsouth.net>
  - emelfm-0.9.2--mdk-Makefile-common.patch
  - put plugins in _libdir not _datadir
  - add feature list
  - fix typos

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.2-3mdk
- typo

* Tue Jan 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9.2-2mdk
- icon

* Wed Jul 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9.2-1mdk
- updated to 0.9.2

* Wed Aug 30 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7.2-2mdk
- v0.7.2
- BM
- macros
* Mon Jun 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-1mdk
- new in contribs
- used srpm provided by Laurent Grawet <laurent.grawet@ibelgique.com>
