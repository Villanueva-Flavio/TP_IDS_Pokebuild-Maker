document.addEventListener('DOMContentLoaded', function() {
    var builds = [
        { id: 1, name: 'Build 1' },
        { id: 2, name: 'Build 2' },
        { id: 3, name: 'Build 3' },
        { id: 4, name: 'Build 4' },
        { id: 5, name: 'Build 5' },
        { id: 6, name: 'Build 6' },
        { id: 7, name: 'Build 7' },
        { id: 8, name: 'Build 8' },
        { id: 9, name: 'Build 9' },
        { id: 10, name: 'Build 10' }
    ];

    var select = document.getElementById('editable-select');
    var deleteBtn = document.getElementById('delete_builds_btn');
    var cancelBtn = document.getElementById('cancel_builds_btn');

    
    function loadBuilds() {
        builds.forEach(function(build) {
            var option = document.createElement('option');
            option.value = build.id;
            option.textContent = build.name;
            select.appendChild(option);
        });
    }

    loadBuilds();

    
    function deleteBuild() {
        var selectedBuild = select.options[select.selectedIndex];
        var buildId = selectedBuild.value;
        var buildName = selectedBuild.textContent;

        
        console.log('Build deleted:', buildName, '(ID:', buildId, ')');
    
        builds = builds.filter(function(build) {
            return build.id !== parseInt(buildId);
        });

        
        select.innerHTML = '';
        loadBuilds();
    }

    
    deleteBtn.addEventListener('click', function() {
        if (select.selectedIndex !== -1) {
            deleteBuild();
        } else {
            alert('Select a build');
        }
    });

    
    cancelBtn.addEventListener('click', function() {
        
        console.log('Cancelled');
    });
});

