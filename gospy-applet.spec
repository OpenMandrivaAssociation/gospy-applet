%define name 	gospy-applet
%define version 0.8.0
%define release %mkrel 4

Summary: 	Web and server monitoring applet
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://gospy-applet.labs.libre-entreprise.org/
License: 	GPLv2+
Group: 		Graphical desktop/GNOME
Source: 	http://labs.libre-entreprise.org/download/gospy-applet/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	ImageMagick pkgconfig GConf2
BuildRequires:	libpanel-applet-devel libglade2.0-devel libgnome-vfs2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  gnutls-devel
BuildRequires:  libgnet2-devel
BuildRequires:	scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:  libesmtp-devel
Requires(post):	GConf2
Requires(post): scrollkeeper
Requires(preun):GConf2
Requires(postun):scrollkeeper

%description
gospy-applet is a GNOME 2 applet monitoring Web pages and servers. It detects
changes in page content, page status, page size, page loading time, IP
address, and so on.

%prep
%setup -q

%build
%configure2_5x --with-gconf-schema-file-dir=$RPM_BUILD_ROOT/%_sysconfdir/gconf --with-gconf-source=$RPM_BUILD_ROOT/%_sysconfdir/gconf
%make

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
rm -fr $RPM_BUILD_ROOT/var/lib/scrollkeeper
mkdir -p $RPM_BUILD_ROOT/etc/gconf/schemas
mv $RPM_BUILD_ROOT/etc/gconf/gospy_applet.schemas $RPM_BUILD_ROOT/etc/gconf/schemas/gospy_applet.schemas
%find_lang %name

%post
%post_install_gconf_schemas %name
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog README NEWS THANKS
%_bindir/%name
%_sysconfdir/gconf/schemas/*
%_libdir/bonobo/servers/*
%_datadir/gnome-2.0/ui/*
%_datadir/gnome/help/%name
%_datadir/%name
%_datadir/omf/%name
%_datadir/pixmaps/*
