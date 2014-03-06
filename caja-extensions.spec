%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname mate-file-manager

Name:           caja-extensions
Summary:        Set of extensions for caja file manager
Version:        1.8.0
Release:        1
Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Source1:        caja-share-setup-instructions
Source2:        caja-share-smb.conf.example

BuildRequires:  mate-common >= 1.7.0
BuildRequires:  pkgconfig(libcaja-extension) >= 1.7.0
BuildRequires:  pkgconfig(mate-desktop-2.0) >= 1.7.0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gupnp-1.0)

%description
Extensions for the caja file-browser, open-terminal,
image-converter, sendto and share

%package common
Summary:    Common files for caja-extensions
Group:      Graphical desktop/Other
BuildArch:  noarch
# gksu support disabled. Suggest caja-actions with open
# as root support.
Suggests:   caja-actions >= 1.6.2-2

%description common
Common files for caja extensions such as 
open-terminal, image-converter etc.

%package -n caja-image-converter
Summary:    Caja extension to mass resize images
Group:	    Graphical desktop/Other
Requires:   %{name}-common = %{version}-%{release}
Requires:   imagemagick
Requires:   %{_lib}caja-extension1 >= 1.7.0
Provides:   %{oname}-image-converter = %{version}-%{release}
Obsoletes:  %{oname}-image-converter < 1.7.0

%description -n caja-image-converter
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.

%package -n caja-open-terminal
Summary:    Caja extension for an open terminal shortcut
Group:	    Graphical desktop/Other
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{_lib}caja-extension1 >= 1.7.0
Provides:   %{oname}-open-terminal = %{version}-%{release}
Obsoletes:  %{oname}-open-terminal < 1.7.0

%description -n caja-open-terminal
This is a proof-of-concept Caja extension which allows you to open
a terminal in arbitrary local folders.

%package -n caja-sendto
Summary:    Send files from caja using with mail or IM
Group:	    Graphical desktop/Other
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{_lib}caja-extension1 >= 1.7.0
Provides:   %{name}-gajim  = %{version}-%{release}
Provides:   %{name}-email = %{version}-%{release}
Provides:   %{name}-evolution = %{version}-%{release}
Provides:   %{oname}-sendto = %{version}-%{release}
Obsoletes:  %{oname}-sendto < 1.7.0
Conflicts:  %{oname}-bluetooth

%description -n caja-sendto
This application provides integration between caja and mail or IM clients.
It adds a Caja context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package -n caja-sendto-pidgin
Summary:    Send files from caja to pidgin
Group:      Graphical desktop/Other
Requires:   pidgin
Requires:   %{name}-common = %{version}
Requires:   caja-sendto = %{version}-%{release}
Provides:   %{name}-sendto-gaim = %{version}-%{release}
Provides:   %{oname}-sendto-pidgin = %{version}-%{release}
Obsoletes:  %{oname}-sendto-pidgin < 1.7.0

%description -n caja-sendto-pidgin
This application provides integration between caja and pidgin.  It
adds a Caja context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package -n caja-sendto-upnp
Summary:    Send files from nautilus via UPNP
Group:      Graphical desktop/Other
Requires:   %{name}-common = %{version}
Requires:   caja-sendto = %{version}-%{release}
Provides:   %{oname}-sendto-upnp = %{version}-%{release}
Obsoletes:  %{oname}-sendto-upnp < 1.7.0

%description -n caja-sendto-upnp
This application provides integration between caja and UPNP.
It adds a Caja context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package -n caja-sendto-devel
Summary:    Development libraries and headers for caja-sendto
Group:	    Development/C
Requires:   %{name}-common = %{version}-%{release}
Requires:   caja-sendto = %{version}-%{release}
Provides:   %{oname}-sendto-devel = %{version}-%{release}
Obsoletes:  %{oname}-sendto-devel < 1.7.0

%description -n caja-sendto-devel
Development libraries and headers for caja-sendto

%package -n caja-share
Summary:    Easy sharing folder via Samba (CIFS protocol)
Group:      Networking/File transfer
Requires:   %{name}-common = %{version}-%{release}
Requires:   %{_lib}caja-extension1 >= 1.7.0
Requires:   samba
Provides:   %{oname}-share = %{version}-%{release}
Obsoletes:  %{oname}-share < 1.7.0

%description -n caja-share
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%prep
%setup -q
cp %{SOURCE1}/caja-share-setup-instructions SETUP

%build
# gksu support disabled. It doesn't work with our gksu-polkit
%configure2_5x \
     --disable-schemas-compile \
     --with-gtk=2.0            \
     --enable-image-converter  \
     --enable-open-terminal    \
     --enable-sendto           \
     --enable-share            \
     --disable-gksu             \
     --disable-static

%make

%install
%makeinstall_std

find %{buildroot} -name *.a -delete

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2}/ %{buildroot}/%{_sysconfdir}/samba/

# remove needless MateConf stuff
rm -fr  %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name

%files common -f %{name}.lang
%doc AUTHORS README SETUP
%dir %{_datadir}/caja-extensions

%files -n caja-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui

%files -n caja-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files -n caja-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%{_mandir}/man1/caja-sendto.1.*

%files -n caja-sendto-pidgin
%{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files -n caja-sendto-upnp
%{_libdir}/caja-sendto/plugins/libnstupnp.so

%files -n caja-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*

%files -n caja-share
%config(noreplace) %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
