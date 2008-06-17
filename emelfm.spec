%define rel 2
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
 
