package com.runclub.runclub.services;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.runclub.runclub.dto.ClubDto;
import com.runclub.runclub.models.Club;
import com.runclub.runclub.repository.ClubRepository;


@Service
public class ClubServiceImpl implements ClubService {
    public ClubRepository clubRepository;

    public ClubServiceImpl(ClubRepository clubRepository) {
        this.clubRepository = clubRepository;
    }

    @Override
    public List<ClubDto> findAllClubs() {
        List<Club> clubs = clubRepository.findAll();
        return clubs.stream().map(club -> mapToClubDto(club)).collect(Collectors.toList());
    }

    private ClubDto mapToClubDto(Club club) {
        return ClubDto.builder().id(club.getId()).title(club.getTitle()).photoUrl(club.getPhotoUrl())
                .content(club.getContent()).createdOn(club.getCreatedOn()).updatedOn(club.getUpdatedOn()).build();
    }
}
