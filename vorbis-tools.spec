Summary:	The Ogg Vorbis Tools
Name:		vorbis-tools
Version:	1.4.0
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# Source0-md5:	567e0fb8d321b2cd7124f8208b8b90e6
Patch0:		%{name}-nolibnsl.patch
URL:		http://www.vorbis.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	flac-devel
BuildRequires:	libao-devel
BuildRequires:	libkate-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality audio. This
package contains various tools for Ogg Vorbis files such as command
line encoder, decoder, player, etc.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

