Summary:	Gnuserv - editing server for Emacs
Summary(pl):	Gnuserv - serwer dla Emacsa
Name:		gnuserv
Version:	3.12.6
Release:	3
License:	GPL v2+
Group:		Applications/Editors/Emacs
Vendor:		Martin Schwenke <martin@meltin.net>
Source0:	http://meltin.net/hacks/emacs/src/%{name}-%{version}.tar.gz
# Source0-md5:	011a6644c193579245ca09eaae8c9850
Patch0:		%{name}-mandir.patch
URL:		http://meltin.net/hacks/emacs/
BuildRequires:	autoconf
Requires:	emacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnuserv allows you to attach to an already running Emacs. This allows
external programs to make use of Emacs' editing capabilities. It is
like GNU Emacs' emacsserver/server.el, but has many more features.

%description -l pl
gnuserv pozwala innym programom po³±czyæ siê z uruchomionym Emacsem.
Umo¿liwia im to korzystanie z Emacsa jako edytora. Jest podobny do
emacsserver/server.el GNU Emacsa, ale du¿o bardziej rozbudowany.

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

%makeinstall install-elisp \
	 elispdir=$RPM_BUILD_ROOT%{_emacs_lispdir}

for man in `find $RPM_BUILD_ROOT%{_mandir} -type l`; do
	target=`readlink $man`
	rm $man
	echo ".so $target" > $man
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.orig ChangeLog
%attr(755,root,root) %{_bindir}/gnuserv
%{_emacs_lispdir}/gnuserv.el
%{_emacs_lispdir}/gnuserv.elc

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_bindir}/gnudoit
%{_mandir}/*/*
