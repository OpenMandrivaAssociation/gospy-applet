%define name 	gospy-applet
%define version 0.9
%define release %mkrel 2

Summary: 	Web and server monitoring applet
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		https://gospy-applet.labs.libre-entreprise.org/
License: 	GPLv2+
Group: 		Graphical desktop/GNOME
Source: 	http://labs.libre-entreprise.org/download/gospy-applet/%{name}-%{version}.tar.gz
Patch0:		gospy-applet-0.8.0-gnutls-2.8.patch
Patch1:		gospy-applet-0.8.0-gnome-ui.patch
Patch2:		gospy-applet-0.8.0-fix-str-fmt.patch
Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	imagemagick pkgconfig GConf2
BuildRequires:	libpanel-applet-devel libglade2.0-devel libgnome-vfs2-devel gnomeui2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  gnutls-devel
BuildRequires:  libgnet2-devel
BuildRequires:	scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:  libesmtp-devel
BuildRequires:	intltool
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
%patch0 -p0
%patch1 -p0
%patch2 -p0
mkdir m4

%build
autoreconf -fi
%configure2_5x --disable-schemas-install
# --with-gconf-schema-file-dir=$RPM_BUILD_ROOT/%_sysconfdir/gconf --with-gconf-source=$RPM_BUILD_ROOT/%_sysconfdir/gconf
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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
