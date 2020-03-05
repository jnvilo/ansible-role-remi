
repos = ['remi-glpi91.repo', 'remi-glpi93.repo', 'remi-modular.repo', 'remi-php70.repo', 'remi-php72.repo', 'remi-php74.repo', 'remi-safe.repo', 'remi-glpi91.repo', 'remi-glpi93.repo', 'remi-modular.repo', 'remi-php70.repo', 'remi-php72.repo', 'remi-php74.repo', 'remi-safe.repo']


for each in repos: 
    tmpl = """
    - name: {}
      template:
        src: "{{{{ role_path }}}}/templates/yum.repos.d/{}.j2"
        dest: /etc/yum.repos.d/{}
        mode: '0644'
        owner: root
        group: root
    """
    print(tmpl.format(each, each , each))


