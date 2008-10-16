%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	High Performance MySQL Tuning Script
Name:		mysqltuner
Version:	0.9.9
Release:	%mkrel 1
Group:		System/Servers
License:	GPLv3+
URL:		http://rackerhacker.com/mysqltuner/
Source0:	http://mysqltuner.com/mysqltuner.pl
Requires:	mysql
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MySQLTuner is a high-performance MySQL tuning script written in perl that will
provide you with a snapshot of a MySQL server's health. Based on the statistics
gathered, specific recommendations will be provided that will increase a MySQL
server's efficiency and performance. The script gives you automated MySQL
tuning that is on the level of what you would receive from a MySQL DBA.

This script has been derived from many of the ideas in Matthew Montgomery's
MySQL tuning primer script.

%prep

%setup -q -c -T

cp %{SOURCE0} %{name}
dos2unix -U %{name}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m0755 %{name} %{buildroot}%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}
