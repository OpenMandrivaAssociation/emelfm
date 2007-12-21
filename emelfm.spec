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
 

(cd $RPM_BUILD_ROOT 
mkdir -p   ./usr/lib/menu
 cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}):\
command="%{name}"\
title="Emelfm"\
longtitle="A GTK file manager"\
needs="x11"\
icon="file_tools_section.png"\
section="System/File Tools"
EOF
)

%find_lang %name

%post
/sbin/ldconfig
%{update_menus}      

%postun
/sbin/ldconfig
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr (-,root,root)
%doc README COPYING ChangeLog
%doc docs/help.txt
%{_bindir}/*
%{_libdir}/menu/*
%_libdir/emelfm/plugins/*.so
 
