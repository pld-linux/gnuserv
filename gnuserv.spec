Summary:	Gnuserv - editing server for Emacs
Summary(pl.UTF-8):	Gnuserv - serwer dla Emacsa
Name:		gnuserv
Version:	3.12.6
Release:	5
License:	GPL v2+
Group:		Applications/Editors/Emacs
Source0:	http://meltin.net/hacks/emacs/src/%{name}-%{version}.tar.gz
# Source0-md5:	011a6644c193579245ca09eaae8c9850
Patch0:		%{name}-mandir.patch
URL:		http://meltin.net/hacks/emacs/
BuildRequires:	autoconf
BuildRequires:	rpmbuild(macros) >= 1.402
Requires:	emacs
Requires:	gnuserv-elisp = %{version}-%{release}
Conflicts:	xemacs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnuserv allows you to attach to an already running Emacs. This allows
external programs to make use of Emacs' editing capabilities. It is
like GNU Emacs' emacsserver/server.el, but has many more features.

%description -l pl.UTF-8
gnuserv pozwala innym programom połączyć się z uruchomionym Emacsem.
Umożliwia im to korzystanie z Emacsa jako edytora. Jest podobny do
emacsserver/server.el GNU Emacsa, ale dużo bardziej rozbudowany.

%package elisp
Summary:	Compiled elisp files for gnuserv
Summary(pl.UTF-8):	Skompilowany kod elisp gnuserv
Group:		Applications/Editors/Emacs
Requires:	%{_bindir}/gnuserv
%requires_eq emacs

%description elisp
Compiled elisp files for gnuserv

%description elisp -l pl.UTF-8
Skompilowany kod elisp gnuserv

%package elisp-el
Summary:	Source elisp files for gnuserv
Summary(pl.UTF-8):	Kod źródłowy elisp gnuserv
Group:		Applications/Editors/Emacs
Requires:	%{name}-elisp = %{version}-%{release}

%description elisp-el
Source elisp files for gnuserv

%description elisp-el -l pl.UTF-8
Kod źródłowy elisp gnuserv

%package client
Summary:	gnuserv client program
Summary(pl.UTF-8):	Program kliencki dla gnuserv
Group:		Applications/Editors/Emacs
Conflicts:	xemacs

%description client
A client program for gnuserv.

%description client -l pl.UTF-8
Program kliencki dla gnuserv.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%{__autoheader}

%configure
echo '#define SYS_SIGLIST_DECLARED 1 /* Kludge! */' >> config.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}

%makeinstall
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}
install *.elc *.el $RPM_BUILD_ROOT%{_emacs_lispdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.orig ChangeLog
%attr(755,root,root) %{_bindir}/gnuserv

%files elisp
%defattr(644,root,root,755)
%{_emacs_lispdir}/*.elc

%files elisp-el
%defattr(644,root,root,755)
%{_emacs_lispdir}/*.el

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_bindir}/gnudoit
%{_mandir}/*/*
