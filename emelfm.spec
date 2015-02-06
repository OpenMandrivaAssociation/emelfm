%define debug_package %{nil}
%define extra_ver 1
%define rversion 0.9.2

Summary:	File manager using the two-panel design and Gtk+
Name:		emelfm
Version:	0.9.2.%{extra_ver}
Release:	7
License:	GPLv2+
Group:		File tools
Url:		http://www.havens.de/elm/emelfm.html
Source0:	%{name}-%{rversion}-elm%{extra_ver}.tar.bz2
BuildRequires:	pkgconfig(gtk+)
Requires:	gtk+
Requires:	xterm

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

%files -f %{name}.lang
%doc README COPYING ChangeLog
%doc docs/help.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_libdir}/emelfm/plugins/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{rversion}-elm%{extra_ver}

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_libdir}/emelfm/plugins
mkdir -p %{buildroot}%{_datadir}/locale/
make BIN_DIR=%{buildroot}%{_bindir} DOC_DIR=%{buildroot}%{_docdir} \
	PLUGINS_DIR=%{buildroot}%{_libdir}/emelfm/plugins \
	LOCALEDIR=%{buildroot}%{_datadir}/locale/ install

rm -rf %{buildroot}%{_docdir}/help.txt

mkdir -p %{buildroot}%{_datadir}/applications/
 cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Name=Emelfm
Comment=A GTK file manager
Icon=file_tools_section
Categories=FileManager;Utility;
EOF

%find_lang %{name}

