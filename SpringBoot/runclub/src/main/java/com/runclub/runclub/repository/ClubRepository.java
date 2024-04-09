package com.runclub.runclub.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.runclub.runclub.models.Club;

public interface ClubRepository extends JpaRepository<Club, Long> {

}
