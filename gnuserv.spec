#
Summary:	Gnuserv - editing server for Emacs
Summary(pl):	Gnuserv - serwer dla Emacsa
Name:		gnuserv
Version:	3.12.6
Release:	2
License:	GPL v2+
Group:		Applications/Editors/Emacs
Vendor:		Martin Schwenke <martin@meltin.net>
Source0:	http://meltin.net/hacks/emacs/src/%{name}-%{version}.tar.gz
# Source0-md5:	011a6644c193579245ca09eaae8c9850
URL:		http://meltin.net/hacks/emacs/
BuildRequires:	autoconf
Requires:	emacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnuserv allows you to attach to an already running Emacs. This allows
external programs to make use of Emacs' editing capabilities. It is
like GNU Emacs' emacsserver/server.el, but has many more features.

%description -l pl
gnuserv pozwala innym programom po��czy� si� z uruchomionym Emacsem.
Umo�liwia im to korzystanie z Emacsa jako edytora. Jest podobny do
emacsserver/server.el GNU Emacsa, ale du�o bardziej rozbudowany.

%package client
Summary:	gnuserv client program
Summary(pl):	Program kliencki dla gnuserv
Group:		Applications/Editors/Emacs

%description client
A client program for gnuserv.

%description client -l pl
Program kliencki dla gnuserv.

%prep
%setup -q

%build
%{__autoconf}
%{__autoheader}

%{configure}
echo '#define SYS_SIGLIST_DECLARED 1 /* Kludge! */' >> config.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_emacs_lispdir}
%{makeinstall} elispdir=$RPM_BUILD_ROOT/%{_emacs_lispdir} install-elisp
%{__mv} $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT/%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.orig ChangeLog
%defattr(644,root,root,755)
%{_emacs_lispdir}/gnuserv.el
%{_emacs_lispdir}/gnuserv.elc
%attr(0755,root,root)%{_bindir}/gnuserv

%files client
%defattr(644,root,root,755)
%attr(0755,root,root)%{_bindir}/gnuclient
%attr(0755,root,root)%{_bindir}/gnudoit
%{_mandir}/*/*
