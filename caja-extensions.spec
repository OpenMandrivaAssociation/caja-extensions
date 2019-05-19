%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname mate-file-manager

# gksu support disabled. It doesn't work with our gksu-polkit
%bcond_with gksu

Summary:	Set of extensions for caja file manager
Name:		caja-extensions
Version:	1.22.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	caja-share-setup-instructions
Source2:	caja-share-smb.conf.example

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gupnp-1.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mate-desktop-2.0)

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides some extensions for the caja file-browser, open-terminal,
image-converter, sendto, share, etc ...

#---------------------------------------------------------------------------

%package common
Summary:	Common files for caja-extensions
Group:		Graphical desktop/Other
BuildArch:	noarch

%description common
Common files for caja extensions such as image-converter, open-terminal,
sendto, sendto-pidgin, sendto-upnp, share, wallpaper.

%files common -f %{name}.lang
%doc AUTHORS README SETUP
%dir %{_datadir}/caja-extensions

#---------------------------------------------------------------------------

%if %{with gksu}
%package -n caja-beesu
Summary:	MATE file manager beesu
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}-%{release}
Requires:	beesu
%rename		%{oname}-beesu

%description -n caja-beesu
Caja beesu extension for open files as superuser

%files -n caja-beesu
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension
%endif

#---------------------------------------------------------------------------

%package -n caja-image-converter
Summary:	Caja extension to mass resize images
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}-%{release}
Requires:	imagemagick
%rename		%{oname}-image-converter

%description -n caja-image-converter
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.

%files -n caja-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

#---------------------------------------------------------------------------

%package -n caja-open-terminal
Summary:	Caja extension for an open terminal shortcut
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}-%{release}
%rename		%{oname}-open-terminal

%description -n caja-open-terminal
This is a proof-of-concept Caja extension which allows you to open
a terminal in arbitrary local folders.

%files -n caja-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension

#---------------------------------------------------------------------------

%package -n caja-sendto
Summary:	Caja extension to send files from caja using with mail or IM
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name}-gajim = %{version}-%{release}
Provides:	%{name}-email = %{version}-%{release}
Provides:	%{name}-evolution = %{version}-%{release}
%rename		%{oname}-sendto

%description -n caja-sendto
This application provides integration between caja and mail or IM clients.
It adds a Caja context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%files -n caja-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
%{_mandir}/man1/caja-sendto.1*

#---------------------------------------------------------------------------

%package -n caja-sendto-pidgin
Summary:	Caja extension to send files from caja to pidgin
Group:		Graphical desktop/Other
Requires:	pidgin
Requires:	%{name}-common = %{version}
Requires:	caja-sendto = %{version}-%{release}
Provides:	%{name}-sendto-gaim = %{version}-%{release}
%rename		%{oname}-sendto-pidgin

%description -n caja-sendto-pidgin
This application provides integration between caja and pidgin. It
adds a Caja context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%files -n caja-sendto-pidgin
%{_libdir}/caja-sendto/plugins/libnstpidgin.so

#---------------------------------------------------------------------------

%package -n caja-sendto-upnp
Summary:	Caja extension to send files from nautilus via UPNP
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}
Requires:	caja-sendto = %{version}-%{release}
%rename		%{oname}-sendto-upnp

%description -n caja-sendto-upnp
This application provides integration between caja and UPNP.
It adds a Caja context menu component ("Send To...") and allows sending
files to UPNP media servers.

%files -n caja-sendto-upnp
%{_libdir}/caja-sendto/plugins/libnstupnp.so

#---------------------------------------------------------------------------

%package -n caja-sendto-devel
Summary:	Development libraries and headers for caja-sendto
Group:		Development/C
Requires:	%{name}-common = %{version}-%{release}
Requires:	caja-sendto = %{version}-%{release}
%rename		%{oname}-sendto-devel

%description -n caja-sendto-devel
Development libraries and headers for caja-sendto

%files -n caja-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*

#---------------------------------------------------------------------------

%package -n caja-share
Summary:	Caja extension to easy sharing folder via Samba (CIFS protocol)
Group:		Networking/File transfer
Requires:	%{name}-common = %{version}-%{release}
Requires:	samba-server
Requires:	gvfs-fuse
Requires:	gvfs-smb
Recommends:	gvfs-mtp
%rename		%{oname}-share

%description -n caja-share
Caja extension designed for easier folders
sharing via Samba (CIFS protocol) in *NIX systems.

%files -n caja-share
%config(noreplace) %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
%{_datadir}/caja/extensions/libcaja-share.caja-extension

#---------------------------------------------------------------------------

%package -n caja-wallpaper
Summary:	Caja extension to set wallpaper for caja
Group:		Graphical desktop/Other
Requires:	%{name}-common = %{version}-%{release}
%rename		%{oname}-wallpaper

%description -n caja-wallpaper
Caja extension for wallpaper.

%files -n caja-wallpaper
%{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension

#---------------------------------------------------------------------------

%package -n caja-xattr-tags
Summary:	Caja extension to easly set xattr-tags
Requires:	%{name}-common = %{version}-%{release}
%rename		%{oname}-xattr-tags

%description -n caja-xattr-tags
Caja xattr-tags extension, allows to quickly set xattr-tags.

%files -n caja-xattr-tags
%{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension

#---------------------------------------------------------------------------

%prep
%setup -q
cp %{SOURCE1} SETUP
%autopatch -p1

%build
%configure \
	--disable-schemas-compile \
	--enable-image-converter \
	--enable-gtk-doc-html \
	--enable-open-terminal \
	--enable-sendto \
	--enable-share \
	--enable-wallpaper \
%if %{without gksu}
	--disable-gksu \
%endif
	--with-sendto-plugins=all \
	%{nil}
%make_build

%install
%make_install

# samba configuration for caja-share
install -dm 0755 %{buildroot}/%{_sysconfdir}/samba/
install -pm 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

# locales
%find_lang %{name} --with-gnome --all-name
