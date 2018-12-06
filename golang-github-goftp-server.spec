# Run tests in check section
# Needs network access
%bcond_with check

# https://github.com/goftp/server
%global goipath         github.com/goftp/server
%global commit          1fd52c8552f108eccff6122276753fc1f24c49ed

%global common_description %{expand:
A FTP server framework written in Golang.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A FTP server framework written in Golang 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  golang(github.com/goftp/file-driver)
BuildRequires:  golang(github.com/jlaffaye/ftp)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md exampleftpd


%changelog
* Sun Oct 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181105git1fd52c8
- First package for Fedora
