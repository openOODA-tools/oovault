Name:           oovault
Version:        0.1.0
Release:        1%{?dist}
Summary:        Encrypted secret vault storing API keys and tokens backed by kernel keyrings.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oovault
Source0:        oovault-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oovault is a sovereign, capability-bounded SECRET STORE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oovault
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oovault-uninstall

%files
/usr/bin/oovault
/usr/bin/oovault-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
