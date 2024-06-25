$(document).ready(function() {
    
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

    
    function loadBuilds() {
        var buildsList = $('#buildsList');
        buildsList.empty(); 

        builds.forEach(function(build) {
            buildsList.append(`<option value="${build.id}">${build.name}</option>`);
        });
    }

    
    loadBuilds();

    
    $('#searchInput').on('input', function() {
        var searchValue = $(this).val().toLowerCase();
        filterBuilds(searchValue);
    });

    
    $('#selectBuildBtn').on('click', function() {
        var selectedBuildId = $('#buildsList').val();
        if (selectedBuildId) {
            var selectedBuildName = $('#buildsList option:selected').text();
            alert(`Build select: ${selectedBuildName} (ID: ${selectedBuildId})`);
            
        } else {
            alert('Select build.');
        }
    });

    
    function filterBuilds(searchValue) {
        $('#buildsList option').each(function() {
            var buildName = $(this).text().toLowerCase();
            var isVisible = buildName.indexOf(searchValue) > -1;
            $(this).toggle(isVisible);
        });
    }
});
